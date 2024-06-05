from typing import Literal

from pydantic import BaseModel, Field

from models.base.image_preview import ImagePreviewModel


class InputModel(BaseModel):
    name: str = Field(
        description='홍길동',
        default='이름',
    )
    gender: Literal['남', '여'] = Field(
        alias='성별',
        description='성별',
        default='남',
    )    
    birth_year: str = Field(
        description='태어난 년도',
        default='2024',
    )
    birth_month: Literal['1월', '2월', '3월', '4월', '5월', '6월', 
                         '7월', '8월', '9월', '10월', '11월', '12월'] = Field(
        alias='태어난 달',
        description='태어난 달',
        default='1월',
    )
    birth_date: Literal['1일', '2일', '3일', '4일', '5일', '6일', 
                         '7일', '8일', '9일', '10일', '11일', '12일', 
                         '13일', '14일', '15일', '16일', '17일', '18일', 
                         '19일', '20일', '21일', '22일', '23일', '24일',
                         '25일', '26일', '27일', '28일', '29일', '30일', 
                         '31일'] = Field(
        alias='태어난 날',
        description='태어난 날',
        default='1일',
    )                     
    birth_time: Literal['23:30~1:29', '1:30~3:29', '3:30~5:29', '5:30~7:29', '7:30~9:29', '9:30~11:29', 
                         '11:30~13:29', '13:30~15:29', '15:30~17:29', '17:30~19:29', '19:30~21:29', '21:30~23:29', 
                         '모름'] = Field(
        alias='태어난 시각',
        description='태어난 시각',
        default='모름',
    )  



class OutputModel(ImagePreviewModel):
    output: str = Field(
        description='응답',
    )
