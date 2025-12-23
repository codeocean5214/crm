from fastapi import HTTPException 
from sqlalchemy.orm import Session 
from crm.models import Deal 
from crm.constants import DealStage, deal_probability_mapping
from crm.repiositories.deal_repo import  DealRepository

class DealServices : 
    def __init__(self) :  
        self.repo = DealRepository() #we are creating a repo instance for importing the functions that we wrote in the repository for db action
    
    def create_deal(self,db:Session,customer_id : int, amount : float,admin ) : 
            active = self.repo.get_deal_active_customer(db, customer_id)
            if active:
                raise HTTPException(
                    400,
                    "Customer already has an active deal"
                )

            deal = Deal(
                customer_id=customer_id,
                amount=amount,
                stage=DealStage.prospecting,
                probability=deal_probability_mapping[DealStage.prospecting],
                expected_value=amount * deal_probability_mapping[DealStage.prospecting],
                owner_id=admin.id
            )

            return self.repo.create(db, deal)
    def advance_stage(self, db: Session, deal_id: int, next_stage: DealStage):
        deal = self.repo.get_deal_by_id(db, deal_id)
        if not deal:
            raise HTTPException(404, "Deal not found")

        if deal.stage in [DealStage.won, DealStage.lost]:
            raise HTTPException(
                400,
                "Closed deals cannot be modified"
            )

        deal.stage = next_stage
        deal.probability = deal_probability_mapping[next_stage]
        deal.expected_value = deal.amount * deal.probability
        try :     
            db.commit()
            return deal
        except Exception as e : 
            print("ERROR OCCURED",e)


    
