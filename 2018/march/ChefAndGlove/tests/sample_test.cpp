//
// Created by ratanparai on 3/11/18.
//

#include "gtest/gtest.h"
#include "src/libmain.h"


TEST(example, failed_test)
{
    EXPECT_TRUE(true);
}

TEST(example, libtest_example)
{
    EXPECT_EQ(8, add(4,4));
}





