from models.today_fortune import InputModel, OutputModel
from utils.page import PageModel


def execute(
    page: PageModel,
    key: str,
    model: InputModel,
) -> OutputModel | None:
    real_val=model
    print("Frontend/functions/today_fortune.py: \n", real_val)
    return page.settings.client.call(
        function=page.function,
        input=real_val,
        output_model=OutputModel,
    )
