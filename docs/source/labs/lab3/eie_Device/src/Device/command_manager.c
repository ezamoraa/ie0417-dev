#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>

#include "uthash.h"
#include "command_manager.h"
#include "command.h"
#include "factory.h"

/** Entry structure to support adding sensors to an UT hash table */
struct DeviceHashEntry {
    struct Device *ddr;
    UT_hash_handle hh;
};

/** Sensor manager structure declaration (not exposed) */
struct DeviceManager {
    struct DeviceManagerConfig cfg;
    cJSON *cfg_cjson;
    struct SensorFactory *sf;
    /** Head entry for the sensor hash table */
    struct DeviceHashEntry *sensor_ht;
};

/** Creates a cJSON handle from the data read from a file */
static cJSON *cjson_handle_create(const char *filename)
{
    int ret;
    FILE *fp;
    int fsize;
    cJSON *cjson = NULL;
    fp = fopen(filename, "r");
    if (fp == NULL) {
        fprintf(stderr, "Failed to open file: %s [%s (%d)]\n",
                filename, strerror(errno), errno);
        return NULL;
    }

    // Get file size in bytes
    if (fseek(fp, 0L, SEEK_END) != 0) {
        fprintf(stderr, "fseek end failed for config file\n");
        fclose(fp);
        return NULL;
    }
    fsize = ftell(fp);

    // Rewind file to start
    if (fseek(fp, 0L, SEEK_SET) != 0) {
        fprintf(stderr, "fseek set failed for config file\n");
        fclose(fp);
        return NULL;
    }

    // Allocate buffer to store file data
    char *fbuf = malloc(fsize);
    if (fbuf == NULL) {
        fprintf(stderr, "Failed to allocate file buffer\n");
        fclose(fp);
        return NULL;
    }

    // Read file data into buffer
    ret = fread(fbuf, sizeof(char), fsize, fp);
    if (!ret) {
        fprintf(stderr, "Failed to read file into buffer [ret=%d][%s (%d)]\n",
                ret, strerror(errno), errno);
        fclose(fp);
        return NULL;
    }
    fclose(fp);

    // Parse JSON from file data
    cjson = cJSON_Parse(fbuf);
    if (cjson == NULL) {
        fprintf(stderr, "Failed to parse json file\n");
        return NULL;
    }
    return cjson;
}

/** Destroys a cJSON handle */
static void cjson_handle_destroy(cJSON* cjson)
{
    cJSON_Delete(cjson);
}

/** Add sensor to the manager's sensor hash table */
static int sensor_ht_add(struct DeviceManager *smgr, struct Sensor *ddr)
{
    struct DeviceHashEntry *entry =
        malloc(sizeof(struct DeviceHashEntry));
    if (entry == NULL) {
        fprintf(stderr, "Failed to allocate sensor hash entry\n");
        return -ENOMEM;
    }
    printf("%s: sensor name=%s, type=%s\n", __func__, ddr->info.name, ddr->info.type);
    entry->ddr = ddr;
    HASH_ADD_KEYPTR(hh, smgr->sensor_ht, ddr->info.name, strlen(ddr->info.name), entry);
    return 0;
}

/** Creates the manager's sensor hash table and populates it with cJSON */
static int sensor_ht_create(struct DeviceManager *smgr)
{
    int ret;
    cJSON *sensors = NULL;
    int num_sensors = 0;

    sensors = cJSON_GetObjectItem(smgr->cfg_cjson, "sensors");
    if (sensors == NULL) {
        fprintf(stderr, "Failed to read sensors array: %s\n", cJSON_GetErrorPtr());
        return -1;
    }

    // Init head entry for sensor hash table
    smgr->sensor_ht = NULL;

    // Iterate over config array to create sensors
    num_sensors = cJSON_GetArraySize(sensors);
    for(int i = 0; i < num_sensors; i++)
    {
        struct Sensor *ddr = NULL;
        cJSON *sensor, *obj;
        char *name, *type;
        sensor = cJSON_GetArrayItem(sensors, i);

        // Read type and name from JSON
        obj = cJSON_GetObjectItem(sensor, "type");
        if (obj == NULL) {
            fprintf(stderr, "Failed to read sensor type: %s\n", cJSON_GetErrorPtr());
            return -1;
        }
        type = cJSON_GetStringValue(obj);

        obj = cJSON_GetObjectItem(sensor, "name");
        if (obj == NULL) {
            fprintf(stderr, "Failed to read sensor name: %s\n", cJSON_GetErrorPtr());
            return -1;
        }
        name = cJSON_GetStringValue(obj);

        // Create sensor and add it to hash table
        ddr = sensor_factory_sensor_create(smgr->sf, type, name);
        if (ddr == NULL) {
            fprintf(stderr, "Failed to create sensor with type: %s, name: %s\n",
                    type, name);
            return -1;
        }
        ret = sensor_ht_add(smgr, ddr);
        if (ret) {
            fprintf(stderr, "Failed to add sensor with type: %s, name: %s\n",
                    ddr->info.type, ddr->info.name);
            return ret;
        }
    }

    return 0;
}

/** Destroys the manager's sensor hash table */
static void sensor_ht_destroy(struct DeviceManager *smgr)
{
    struct DeviceHashEntry *entry, *tmp;
    HASH_ITER(hh, smgr->sensor_ht, entry, tmp) {
        HASH_DEL(smgr->sensor_ht, entry);
        free(entry);
    }
}

struct DeviceManager *sensor_manager_create(struct DeviceManagerConfig *cfg)
{
    int ret;
    cJSON *cjson = NULL;
    struct DeviceManager *smgr =
        (struct DeviceManager *)calloc(1, sizeof(struct DeviceManager));
    if (smgr == NULL) {
        fprintf(stderr, "Failed to allocate sensor manager\n");
        return NULL;
    }
    smgr->cfg = *cfg;

    cjson = cjson_handle_create(smgr->cfg.cfg_filename);
    if (cjson == NULL) {
        fprintf(stderr, "Failed to create config JSON handle\n");
        return NULL;
    }
    smgr->cfg_cjson = cjson;

    smgr->sf = sensor_factory_create();
    if (smgr->sf == NULL) {
        fprintf(stderr, "Failed to create sensor factory\n");
        return NULL;
    }

    ret = sensor_ht_create(smgr);
    if (ret) {
        fprintf(stderr, "Failed to create sensor hash table with ret=%d\n", ret);
        return NULL;
    }

    return smgr;
}

struct Sensor *sensor_manager_sensor_get(struct DeviceManager *smgr,
                                         const char *name)
{
    struct DeviceHashEntry *entry = NULL;
    HASH_FIND(hh, smgr->sensor_ht, name, strlen(name), entry);
    if (entry == NULL) {
        fprintf(stderr, "Sensor entry not found for name: %s\n", name);
        return NULL;
    }
    return entry->ddr;
}

/** Sensor read command private data */
struct ssr_read_cmd_data {
    struct Sensor *ddr;
};

/** Sensor read command execute function */
static int ssr_read_cmd_exec_fn(void *data)
{
    struct ssr_read_cmd_data *cmd_data = data;
    struct Sensor *ddr = cmd_data->ddr;
    double val = sensor_read(ddr);
    printf("Sensor read command: [%s]: %s: %f %s\n",
           ddr->info.type, ddr->info.name, val, ddr->info.unit);
    return 0;
}

struct Command *sensor_manager_read_cmd_create(
    struct DeviceManager *smgr,
    const char *name)
{
    struct ssr_read_cmd_data *cmd_data = malloc(sizeof(struct ssr_read_cmd_data));
    if (cmd_data == NULL) {
        fprintf(stderr, "Failed to allocate sensor read command data\n");
        return NULL;
    }
    struct Sensor * ddr = sensor_manager_sensor_get(smgr, name);
    if (ddr == NULL) return NULL;
    cmd_data->ddr = ddr;

    return command_create(cmd_data, ssr_read_cmd_exec_fn);
}

void sensor_manager_destroy(struct DeviceManager *smgr)
{
    sensor_ht_destroy(smgr);
    sensor_factory_destroy(smgr->sf);
    cjson_handle_destroy(smgr->cfg_cjson);
    free(smgr);
}