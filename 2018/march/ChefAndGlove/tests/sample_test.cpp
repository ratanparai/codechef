//
// Created by ratanparai on 3/11/18.
//

#include "gtest/gtest.h"
#include "libtest/calc.h"


TEST(example, failed_test)
{
    EXPECT_TRUE(false);
}

TEST(example, libtest_example)
{
    EXPECT_EQ(4, mul(2,2));
}





