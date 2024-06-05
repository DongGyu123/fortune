import os

from fastapi import APIRouter

from llm.chat import build as build_chat
from llm.store import LLMStore
from models.today_fortune import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

###############################################
#                   Actions                   #
###############################################


@router.post(f'/func/{NAME}')
async def call_today_fortune(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build_chat(
        name=NAME,
        llm=store.get('chatgpt'),
    )

    input = f'''
        # About Me
        * Name: {model.name}
        * Gender: {model.gender}
        * Birth Year: {model.year}
        * Birth Month: {model.month}
        * Birth Date: {model.date}
        * Birth Time: {model.time}
    '''

    return OutputModel(
        output = chain.invoke({
            'input_context': input,
        })
    )