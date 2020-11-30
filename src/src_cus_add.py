from .shared_assets.sub_add import sub_add


def src_cus_add(a, b):
    print("")
    print("project 2called_from src_cus_add")
    return a + b


def src_call_sub_add(a, b):
    print("")
    print("project 2 called from src_call_sub_add")
    return sub_add(a, b)
