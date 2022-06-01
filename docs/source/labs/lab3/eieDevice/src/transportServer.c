/*
 * This is the script for TransportServer socket server for the Device
 * instance.
 * It relies on a pthread to process the socket messages.
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <errno.h>
#include <czmq.h>

/* Message types to set in the test_msg_req type field */
enum test_msg_type {
  TEST_MSG_TYPE_A,
  TEST_MSG_TYPE_B,
  TEST_MSG_TYPE_C,
  TEST_MSG_TYPE_MAX,
};

/* Message request structure */ 
struct test_msg_req {
  uint8_t type;
  uint32_t val;
} __attribute((packed));

/* Message response structure */
struct test_msg_resp {
  uint64_t val_a;
  uint8_t val_b;
} __attribute__((packed));

/* Server thread data */
struct server_data {
  pthread_t tid;
  zsock_t *server;
};

int main(int argc, char **argv){
  printf("Hello from server");
}
  
