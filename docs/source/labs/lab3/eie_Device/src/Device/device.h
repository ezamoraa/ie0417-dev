#ifndef DEVICE_H_
#define DEVICE_H_

/** General information related to a sensor */
struct DeviceInfo {
    const char * name;
    const char * cmd_manager;
};

/** Device operations to implement specific device types */
struct DeviceOps {
    /** Read a sample from the Device */
    double (*read)(struct DeviceInfo *info, void *priv);
};

/** Device structure */
struct Device {
    /** Device information */
    struct DeviceInfo info;
    /** Device operations */
    struct DeviceOps *ops;
    /** Device private data passed to ops */
    void *priv;
};

/**
 * Creates a sensor
 *
 * A sensor can be read according to a custom operation
 * and holds generic information about its name, type and
 * measurement unit.
 *
 * @param info Device information structure.
 * @param ops  Device operations.
 * @param priv Device private data.
 *
 * @return Pointer to a sensor manager structure.
 */
struct Device *device_create(struct DeviceInfo *info,
                             struct DeviceOps *ops,
                             void *priv);

/**
 * Reads the sensor
 *
 * @param ssr Device structure.
 *
 * @return Value representing the sensor measurement.
 */
double device_read(struct Device *ssr);

/**
 * Destroys the sensor
 *
 * @param ssr Device structure.
 */
void device_destroy(struct Device *ssr);

#endif // SENSOR_H_