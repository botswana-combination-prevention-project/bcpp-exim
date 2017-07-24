# from ...m2m_recipe import M2mRecipe
from ...model_recipe import ModelRecipe
from ...recipe import site_recipes
from .common_choices import common_choices

df_drop_columns = []

df_add_columns = []

df_rename_columns = {}

df_apply_functions = {
    'why_no_hiv_test': lambda row: common_choices(row['why_no_hiv_test']),
    'hiv_pills': lambda row: common_choices(row['hiv_pills']),
    'arvs_hiv_test': lambda row: common_choices(row['arvs_hiv_test']),
}


m2m_recipes = []

site_recipes.register(ModelRecipe(
    model_name='bcpp_subject.hivuntested',
    df_drop_columns=df_drop_columns,
    df_add_columns=df_add_columns,
    df_rename_columns=df_rename_columns,
    df_apply_functions=df_apply_functions,
    m2m_recipes=m2m_recipes,
))
