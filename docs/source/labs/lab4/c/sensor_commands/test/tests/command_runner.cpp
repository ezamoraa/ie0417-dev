#include "gtest/gtest.h"

#include <sensor_commands/command.h>
#include <sensor_commands/command_runner.h>
#include <sensor_commands/sensor/sensor.h>
#include <sensor_commands/sensor/manager.h>
#include <testutil/rand_gen.hpp>

/** Fixture class for sensor_commands/ command_runner test */
class command_runner_fixture : public testing::Test
{
 protected:
    /* Fixture class members, accesible from test functions */
    int value;
    testutil::rand_gen rng;
    struct CommandRunner *cmd_runner;
    int ret;
    struct CommandRunnerConfig cmd_runner_cfg;
    
    /* Fixture class constructor */
    /* NOTE: Using reproducible random value for seed, check
     * explanation in unittest_main.cpp for more details */
    command_runner_fixture()
        : value(2), rng(rand())
    {
        std::cout << "Test fixture constructor! "<< std::endl;
        std::cout << "  RNG seed " << rng.get_seed() << std::endl;
    }

    virtual void SetUp() {
        int q_size = int(rng.get_rnd_u64_range(1, 1000));
        cmd_runner_cfg = {
            .q_max_size = q_size,
        };
        printf("Q is this size: %d\n",q_size);
        cmd_runner = command_runner_create(&cmd_runner_cfg);
        command_runner_start(cmd_runner);


        std::cout << "Command Runner fixture SetUp! "<< std::endl;
        /* NOTE: Both the constructor and SetUp methods are called for each test.
         * Check Googletest FAQ for more details on when to use each one:
         * https://github.com/google/googletest/blob/main/docs/faq.md#should-i-use-the-constructordestructor-of-the-test-fixture-or-setupteardown-ctorvssetup */
    }

    virtual void TearDown() {
        command_runner_destroy(cmd_runner);

        std::cout << "CommandRunner fixture TearDown! "<< std::endl;
        /* NOTE: Both the destructor and TearDown methods are called for each test.
         * Check Googletest FAQ for more details on when to use each one:
         * https://github.com/google/googletest/blob/main/docs/faq.md#should-i-use-the-constructordestructor-of-the-test-fixture-or-setupteardown-ctorvssetup */
    }
};

TEST_F(command_runner_fixture, create_destroy)
{
    struct CommandRunner *cmd_runner_test(NULL);
    if(cmd_runner_test != NULL){
        ret++;
    }
    if(command_runner_destroy(NULL) != -1){
        ret++;
    }
    ASSERT_EQ(ret,0);
}

TEST_F(command_runner_fixture, start_stop)
{
    ret = command_runner_start(NULL);
    ASSERT_EQ(ret, -1);

    ret = command_runner_start(cmd_runner);
    ASSERT_EQ(ret, 0);

    ret = command_runner_stop(NULL);
    ASSERT_EQ(ret, -1);

    ret = command_runner_stop(cmd_runner);
    ASSERT_EQ(ret, 0);
}

TEST_F(command_runner_fixture, command_send_single)
{
    struct Command *cmd_msg_ret = msg_command_create("Test Message\n");

    ret = command_runner_start(cmd_runner);
    if(ret){
        
        fprintf(stderr, "Failed start: %d\n", ret);
        ASSERT_EQ(ret, 0);
    }

    ret = command_runner_send(NULL, cmd_msg_ret);
    if (ret != -1){
        fprintf(stderr, "Sent msg to Null cmd_runner");
        ASSERT_EQ(ret, -1);
    }

    ret = command_runner_send(cmd_runner, NULL);
    if (ret != -1){
        fprintf(stderr, "Sent Null message to cmd_runner: %d\n", ret);
        ASSERT_EQ(ret, -1);
    }

    ret = command_runner_send(cmd_runner, cmd_msg_ret);
    if(ret){
        fprintf(stderr, "Failed command sent: %d\n", ret);
        ASSERT_EQ(ret, 0);
    }

    command_destroy(cmd_msg_ret);
    ret = command_runner_stop(cmd_runner);
    if(ret){
        fprintf(stderr, "Stop failed cmd_runner: %d\n", ret);
        ASSERT_EQ(ret, 0);
    }
}
