#ifndef COMMAND_H_
#define COMMAND_H_
#include <cjson/cJSON.h>

/** Type of the function that a command can execute */
typedef void (*cmd_exec_fn)(const char *name, void *priv, const char *req_msg, char *resp_msg);

/** Command structure definition */
struct Command {
    /** Private data to pass to the execute function */
    void *data;
    /** Pointer to the command execute function */
    cmd_exec_fn execute;
};

/**
 * Creates a generic command
 *
 * A command encapsulates the information required to
 * execute a command function.
 *
 * @param data    Private data to be passed to the command execute function
 * @param execute Pointer to the command execute function
 *
 * @return Pointer to a command structure.
 */
struct Command *command_create(const char *name, void *priv, const char *req_msg, char *resp_msg);

/**
 * Executes the command function
 *
 * @param cmd command structure.
 */
void command_execute(const char *name, void *priv, const char *req_msg, char *resp_msg);

/**
 * Destroys the command
 *
 * @param cmd command structure.
 */
void command_destroy(const char *name, void *priv, const char *req_msg, char *resp_msg);

/**
 * Creates a message command
 *
 * A message command prints a message when executed.
 * It should be destroyed using the command_destroy API.
 *
 * @param msg     Message to be printed
 *
 * @return Pointer to a command structure.
 */
struct Command *msg_command_create(const char *name, void *priv, const char *req_msg, char *resp_msg);

#endif // COMMAND_H_
