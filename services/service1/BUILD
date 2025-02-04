python_sources(
    name="service1", 
    sources=["src/**/*.py"], 
    dependencies=[
        "//shared/library1:library1"
    ]
)

python_tests(
    name="tests",
    sources=["tests/**/*.py"],
    dependencies=[":service1"]
)

pex_binary(
    name="binary",
    entry_point="service1.main",
    dependencies=[
        ":service1",
    ],
)