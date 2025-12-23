#this file bascially stores all the constants used in crm core module 
#kind off hard coded values ya buisness logic constans
from enum import Enum
#for this mvp we write the constants for the lead first 
#we can come upon these contacts based on the status of the lead found by the sales team
class LeadStatus(Enum): 
    new = "new"
    contacted = "contacted"
    qualified = "qualified"
    converted = "converted"
    lost = "lost"

#thse contacts can be reached by different methods that are listed below
class ContactMethod(Enum):
    email = "email"
    phone = "phone"
    in_person = "in_person"
    social_media = "social_media"
#rhe contatns for the deal stage are satd below 
class DealStage(Enum): 
    won = "won"
    lost = "lost"
    proposal_sent = "proposal_sent"
    negotiation = "negotiation"
    prospecting = "prospecting"
#this is the guess estimated of the various stages of the deal being successful 
deal_probability_mapping = { 
    DealStage.won: 100,
    DealStage.lost: 0,
    DealStage.proposal_sent: 70,
    DealStage.negotiation: 50,
    DealStage.prospecting: 20
}




