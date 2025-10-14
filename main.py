from fastapi import FastAPI
from uuid import uuid4, UUID
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Bonus(BaseModel):
    id: UUID
    name: str
    link: str
    referralCode: str
    expired: bool
    imageURL: str
    claim: str
    description: str
    amount: int
    tag: str


bonuses: List[Bonus] = [
    Bonus(
        id=uuid4(),
        name="BuddyBank", 
        link="https://www.buddy.unicredit.it", 
        referralCode="APL2025", 
        expired=False, 
        imageURL="https://play-lh.googleusercontent.com/NXsVzRkiAXdi3DMll0e9-lrilzPC0MWSf3ZOb8EzqsHQ6dy1x_Vp7jHB22TY0f61kvKV",
        claim="Get €50 on first purchase",
        description="This is BuddyBank",
        amount=50,
        tag="bank"
        ),
    Bonus(
        id=uuid4(), 
        name="Sisal", 
        link="https://www.sisal.it", 
        referralCode="SIL2025", 
        expired=False, 
        imageURL="https://www.romagiallorossa.it/wp-content/uploads/2024/02/sisal-logo.jpg",
        claim="Take the bonus",
        description="This is Sisal",
        amount=100,
        tag="betting"
        ),
    Bonus(
        id=uuid4(), 
        name="Revolut", 
        link="https://www.revolut.com/it-IT/", 
        referralCode="REV2025", 
        expired=False, 
        imageURL="https://images.squarespace-cdn.com/content/v1/6576ee804a4a13284e8d6af6/1adfd922-c96f-401f-8dea-4624ef4da61c/Revolut-logo.png",
        claim="Get $100",
        description="This is Revolut",
        amount=100,
        tag="betting"
        )
]

@app.get("/bonuses", response_model=List[Bonus])
async def get_bonuses():
    return bonuses

@app.post("/bonuses", response_model=Bonus)
async def add_bonus(bonus: Bonus):
    bonuses.append(bonus)
    return bonus

@app.get("/health")
async def health_check():
    return {"status": "healthy"}