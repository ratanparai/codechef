cc_binary(
    name = "main",
    srcs = ["main.cpp"],
    deps = [
        "//src:libmain",
    ],
)

cc_library(
    name = "libmain",
    srcs = ["libmain.cpp"],
    hdrs = ["libmain.h"],
    visibility = ["//visibility:public"],
)

cc_binary(
    name = "distmain",
    srcs = [":gensrcfile"],
)

genrule(
    name = "gensrcfile",
    srcs = [
        "gendist.py",
        "main.cpp",
        "libmain.cpp",
        "libmain.h",
    ],
    outs = ["dist.cpp"],
    cmd = """
            python $(location gendist.py)
            cp dist.cpp $@
          """,
)
