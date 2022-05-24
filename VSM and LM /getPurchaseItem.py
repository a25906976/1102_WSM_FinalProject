import pandas as pd

class getPurchaseItem:
  df = None
  
  def __init__(self,):
    df = pd.read_csv('./dressipi_recsys2022/train_purchases.csv')

  # input sessionID and output the purchase item of this session.  
  def get_purchase(sessionID):
    sessionID = int(sessionID.replace(".txt",""))
    return int(df[df['session_id'] == sessionID].item_id)
  
#p = getPurchaseItem()
#print(p.get_purchase("13.txt"))
