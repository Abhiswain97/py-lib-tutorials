import example_py
import timeit

cy = timeit.timeit("example_cy.test(5)", setup="import example_cy", number=1000)
py = timeit.timeit("example_py.test(5)", setup="import example_py", number=1000)


print(f"Cythonis {py/cy}x faster")
