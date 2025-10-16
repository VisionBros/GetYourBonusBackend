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
        link="https://apps.apple.com/it/app/buddy-unicredit/id1254438272?l=en-GB", 
        referralCode="E0CD49", 
        expired=False, 
        imageURL="https://play-lh.googleusercontent.com/NXsVzRkiAXdi3DMll0e9-lrilzPC0MWSf3ZOb8EzqsHQ6dy1x_Vp7jHB22TY0f61kvKV",
        claim="Offerta valida fino al 23/10/2025",
        description="Scarica l'app e iserisci il codice. Ricevi 50€ con un minimo di 10€ di spesa.",
        amount=50,
        tag="bank"
        ),
    Bonus(
        id=uuid4(), 
        name="Revolut", 
        link="https://revolut.com/referral/?referral-code=llangella00!OCT1-25-AR-MDL-ROI&geo-redirect", 
        referralCode="", 
        expired=False, 
        imageURL="https://images.squarespace-cdn.com/content/v1/6576ee804a4a13284e8d6af6/1adfd922-c96f-401f-8dea-4624ef4da61c/Revolut-logo.png",
        claim="Offerta valida fino al 21/10/2025",
        description="Fai 3 acquisti di almeno 5€ l'uno e ottieni 50€.",
        amount=50,
        tag="bank"
        ),
    Bonus(
        id=uuid4(), 
        name="Test", 
        link="https://revolut.com/referral/?referral-code=llangella00!OCT1-25-AR-MDL-ROI&geo-redirect", 
        referralCode="", 
        expired=False, 
        imageURL="https://images.squarespace-cdn.com/content/v1/6576ee804a4a13284e8d6af6/1adfd922-c96f-401f-8dea-4624ef4da61c/Revolut-logo.png",
        claim="TEST",
        description="TEST",
        amount=100,
        tag="test"
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