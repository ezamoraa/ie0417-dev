#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <linux/limits.h>
#include <czmq.h>

#include <sensor_commands/version.h>
#include <sensor_commands/command.h>
#include <sensor_commands/command_runner.h>
#include <sensor_commands/sensor/sensor.h>
#include <sensor_commands/sensor/manager.h>

/* Message types to set in the test_msg_req type field */
enum test_msg_type {
  TEST_MSG_TYPE_A,
  TEST_MSG_TYPE_B,
  TEST_MSG_TYPE_C,
  TEST_MSG_TYPE_MAX,
};

/* Message request structure */
struct test_msg_req {
    char type[32];
    uint32_t val;
} __attribute__((packed));

/* Message response structure */
struct test_msg_rep {
    uint32_t val_a;
    uint8_t val_b;
} __attribute__((packed));

/* Server thread data */
struct server_data {
    pthread_t tid;
    zsock_t *server;
};

void* msg_server_fn(void *arg)
{
    int ret;
    struct server_data *rdata = arg;
    printf("Thread %ld started\n", rdata->tid);

    rdata->server = zsock_new(ZMQ_REP);
    printf("EL PUNTERO ES: %p \n", rdata->server);
    zsock_bind(rdata->server, "tcp://*:5555");

    /* Loop processing messages while CZMQ is not interrupted */
    while (!zsys_interrupted) {
        zframe_t *req_frame, *rep_frame;
        struct test_msg_req *req;
        struct test_msg_rep *rep;

        // Block waiting for a new message frame
        req_frame = zframe_recv(rdata->server);
        if (!req_frame) {
            fprintf(stderr, "req_frame is NULL\n");
            goto out;
        }
        req = (struct test_msg_req *)zframe_data(req_frame);

        printf("Received request [type: %s, val: %u]\n",
               req->type, req->val);

        rep_frame = zframe_new(NULL, sizeof(struct test_msg_rep));
        rep = (struct test_msg_rep *)zframe_data(rep_frame);

        // Write response data
        rep->val_a = req->val;
        rep->val_b = req->val;

        // No longer need request frame
        zframe_destroy(&req_frame);

        // Sending destroys the response frame
        ret = zframe_send(&rep_frame, rdata->server, 0);
        if (ret) {
            fprintf(stderr, "Failed to send msg with: %d\n", ret);
            goto out;
        }
    }

out:
    zsock_destroy(&rdata->server);
    zsys_interrupted = 1;
    printf("Thread %ld finished\n", rdata->tid);
    return NULL;
}

// int thread_server_run(){
//     int ret;
//     struct server_data rdata = {};
//     const uint32_t sleep_ms = 1000;

//     ret = pthread_create(&(rdata.tid), NULL, &msg_server_fn, &rdata);
//     if (ret != 0) {
//         fprintf(stderr, "Failed to create thread :[%s]", strerror(ret));
//         return ret;
//     }
//     /* zsys_interrupted is a global variable from the czmq library that is set
//      * when the process receives an interrupt signal (SIGINT). This logic
//      * is to stop the program, for example, when the user sends a keyboard
//      * interrupt (Ctrl-C).
//      */
//     while(!zsys_interrupted) {
//         zclock_sleep(sleep_ms);
//     }
//     /* We need some mechanism to stop the server thread that is likely blocked
//      * waiting on I/O (new message). Pthread kill sends a signal to a specific thread,
//      * which is used to interrupt the blocking zframe_recv call that waits for
//      * a new message. When zframe_recv is interrupted it returns a NULL frame, which
//      * we detect to break out of the thread's infinite loop.
//      *
//      * NOTE: An alternative, and maybe safer, approach would be to use a zpoller
//      * with a timeout to avoid blocking the server thread indefinitely,
//      * plus a stop boolean flag to break out of the while loop. We could
//      * also use a high-level CZMQ threaded mechanism (like zloop) to process messages,
//      * but that would defeat the purpose of this example (to use pthread) */
//     pthread_kill(rdata.tid, SIGINT);
//     pthread_join(rdata.tid, NULL);

//     return 0;
// }

static int basic_command_experiment(void)
{
    int ret;

    struct CommandRunnerConfig cmd_runner_cfg = {
      .q_max_size = 100,
    };
    struct CommandRunner *cmd_runner = command_runner_create(&cmd_runner_cfg);
    if (cmd_runner == NULL) {
        fprintf(stderr, "Failed to create command runner\n");
        return -1;
    }
    struct Command *msg_cmd = msg_command_create("This is a command test message!\n");
    if (msg_cmd == NULL) {
        fprintf(stderr, "Failed to create message command\n");
        return -1;
    }

    printf("++++++++++ CommandRunner experiment ++++++++++\n");

    ret = command_runner_start(cmd_runner);
    if (ret) {
        fprintf(stderr, "Failed to start command runner with ret=%d\n", ret);
        return -1;
    }

    for (int i=0; i < 10; i++) {
        ret = command_runner_send(cmd_runner, msg_cmd);
        if (ret) {
            fprintf(stderr, "Failed to send command to command runner with ret=%d\n", ret);
            return -1;
        }
    }

    ret = command_runner_stop(cmd_runner);
    if (ret) {
        fprintf(stderr, "Failed to stop command runner with ret=%d\n", ret);
        return -1;
    }

    command_destroy(msg_cmd);
    command_runner_destroy(cmd_runner);

    return 0;
}

static int sensor_command_experiment(const char *cfg_filename)
{
    int ret;
    struct SensorManagerConfig smgr_cfg = {};
    struct SensorManager *smgr = NULL;
    struct Command *cmd = NULL;

    #define NUM_SENSORS 5

    const char *sensor_names[NUM_SENSORS] = {
      "level-eie202",
      "temp-eie206",
      "temp-eie204",
      "level-eie301",
      "temp-eie208",
    };
    struct Command *commands[NUM_SENSORS] = {
    };

    struct CommandRunnerConfig cmd_runner_cfg = {
      .q_max_size = 100,
    };
    struct CommandRunner *cmd_runner = command_runner_create(&cmd_runner_cfg);
    if (cmd_runner == NULL) {
        fprintf(stderr, "Failed to create command runner\n");
        return -1;
    }

    // thread_server_run();

    printf("++++++++++ SensorManager experiment ++++++++++\n");

    ret = command_runner_start(cmd_runner);
    if (ret) {
        fprintf(stderr, "Failed to start command runner with ret=%d\n", ret);
        return -1;
    }

    smgr_cfg.cfg_filename = cfg_filename;
    smgr = sensor_manager_create(&smgr_cfg);
    if (smgr == NULL) {
        fprintf(stderr, "Failed to create sensor manager\n");
        return -1;
    }

    for (int i=0; i < NUM_SENSORS; i++) {
        const char *name = sensor_names[i];
        if (strlen(name) == 0) break;

        cmd = sensor_manager_read_cmd_create(smgr, name);
        if (cmd != NULL) {
            commands[i] = cmd;
            ret = command_runner_send(cmd_runner, cmd);
            if (ret) {
                fprintf(stderr, "Failed to send command to command runner with ret=%d\n", ret);
                return -1;
            }
        } else {
            printf("Failed to get read command for sensor with name %s\n", name);
        }
    }

    ret = command_runner_stop(cmd_runner);
    if (ret) {
        fprintf(stderr, "Failed to stop command runner with ret=%d\n", ret);
        return -1;
    }

    for (int i=0; i < NUM_SENSORS; i++) {
        command_destroy(commands[i]);
        commands[i] = NULL;
    }

    sensor_manager_destroy(smgr);
    command_runner_destroy(cmd_runner);

    return 0;
}

int main(int argc, char **argv) {
    int opt;
    int ret = 0;
    const char *version = NULL;
    char cfg_filename[PATH_MAX + 1];

    // Parse cmdline options
    while((opt = getopt(argc, (char *const *)argv, "c:")) != -1) {
        switch(opt) {
            case 'c':
                strncpy(cfg_filename, optarg, PATH_MAX);
                break;
            default :
                (void)fprintf(stderr, "Unknown option -%c\n", opt);
                return -EINVAL;
        }
    }

    // Check library version
    ret = sensor_commands_version(&version);
    if (ret) return ret;
    printf("lib version: %s\n", version);

    // Experiment with basic commands
    basic_command_experiment();

    // Experiment with sensor commands
    sensor_command_experiment(cfg_filename);

    return ret;
}
