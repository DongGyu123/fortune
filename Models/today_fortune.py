from typing import Literal

from pydantic import BaseModel, Field

class InputModel(BaseModel):
    name: str = Field(
        default='홍길동',
    )
    gender: Literal[
        '남',
        '여',
    ] = Field(
        default='남',
    )
    
    year: str = Field(
        default='2024',
    )
    month: Literal[
        '1월', '2월','3월','4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월',
    ] = Field(
        default='1월',
    )
    date: Literal[
        '1일', '2일', '3일', '4일', '5일', '6일', '7일', '8일', '9일', '10일', '11일', '12일', '13일', 
        '14일', '15일', '16일', '17일', '18일', '19일', '20일', '21일', '22일', '23일', '24일',
        '25일', '26일', '27일', '28일', '29일', '30일', '31일'
    ] = Field(
        default='1일',
    )

    time: Literal['23:30~01:29', '1:30~3:29', '3:30~5:29', '5:30~7:29', '7:30~9:29', '9:30~11:29', '11:30~13:29', 
                      '13:30~15:29', '15:30~17:29','17:30~19:29', '19:30~21:29', '21:30~23:29', '모름'] = Field(
        default='모름',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description='오늘의 운세',
    )
