from ...model_recipe import ModelRecipe
from ...recipe import site_recipes


site_recipes.register(ModelRecipe(
    model_name='household.householdlog',
    old_model_name='bcpp_household.householdlog',
))
