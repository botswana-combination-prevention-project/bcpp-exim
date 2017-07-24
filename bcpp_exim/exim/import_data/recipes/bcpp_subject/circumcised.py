# from ...m2m_recipe import M2mRecipe
from ...model_recipe import ModelRecipe
from ...recipe import site_recipes
from .common_choices import common_choices

df_drop_columns = []

df_add_columns = []

df_rename_columns = {}

df_apply_functions = {
    'age_unit_circ': lambda row: common_choices(row['age_unit_circ']),
    'where_circ': lambda row: common_choices(row['where_circ']),
    'why_circ': lambda row: common_choices(row['why_circ']),
    'circumcised': lambda row: common_choices(row['circumcised']),
}


m2m_recipes = []

site_recipes.register(ModelRecipe(
    model_name='bcpp_subject.circumcised',
    df_drop_columns=df_drop_columns,
    df_add_columns=df_add_columns,
    df_rename_columns=df_rename_columns,
    df_apply_functions=df_apply_functions,
    m2m_recipes=m2m_recipes,
))
