class Category:
  def __init__(self,category_name):
    self.category_name=category_name
    self.ledger=[]

  def deposit(self,amount,description=''):
    self.ledger.append({"amount": amount, "description": description})
  def sum_ledger(self):
    sumledger=0
    for l in self.ledger:
      sumledger+=float(l["amount"])
    return sumledger
  
  def withdraw(self,amount,description=''):
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": -abs(amount), "description": description})
      return True
    else:
      return False
  def get_balance(self):
    sumledger=0
    for l in self.ledger:
      sumledger+=float(l["amount"])
    return sumledger
  
  def transfer(self,amount,other):
    if self.check_funds(amount)==True:
      self.withdraw(amount,"Transfer to "+str(other.category_name))
      other.deposit(amount,"Transfer from "+str(self.category_name))
      return True
    else:
      return False

  def check_funds(self,amount):
    sumledger=self.sum_ledger()
    if sumledger - float(amount)>=0:
      return True
    else:
      return False

  def __str__(self):
    title=''
    lines=''
    total_line=''
    
    if len(self.category_name)%2==0:
        title=int((30-len(self.category_name))/2)*'*'+self.category_name+int((30-len(self.category_name))/2)*'*'
      
    for l in self.ledger:
    
    
        description_line=l["description"][0:23]+(23-(len(l["description"])))*' '
        amount_line=(7-len("{:.2f}".format(l['amount'])))*' '+"{:.2f}".format(l['amount'])
        lines=lines+(description_line+amount_line)+"\n"
    

    total_line="Total: "+"{:.2f}".format(self.get_balance())
    
    return title+"\n"+lines+total_line

def Perc_1(total, amt):
        amt=float(amt)
        total=float(total)
        perc = float(amt / total) * 100
        perc = int(perc)
        if perc < 10:
            perc = "0"
        else:
            perc = str(perc)[0] + "0"
        
        return int(perc)

def myround(x, base=10):
    return base * round(float(x) / base)

def create_spend_chart(categories):
    perc=0
    val=0 
    perc_list_5=[]             
    for x in categories:
        val=0
        for v in x.ledger:
            if v["amount"]<0:
                d=x.category_name
                val=val+abs(v["amount"]) 
        perc_list_5.append([d,val])

    total_5=sum(row[1] for row in perc_list_5)

    for x in perc_list_5:
       x[1]=Perc_1(total_5,x[1])   
    perc=[]   
    for i in range(100,-10,-10):
        perc.append(i)
    finals=[]
    finals.append("Percentage spent by category\n")
    final1=''
    for p in perc:
      final1=''
      for x in perc_list_5:
        if x[1]>=p:
          final1=final1+" o "
        else:
          final1=final1+"   "
      finals.append("{0:>3}".format(str(p))+"|"+final1+" \n")
    
    lens=[len(x[0]) for x in perc_list_5]
    perc_2=[x[0] for x in perc_list_5]
    perc_3=[x+' '*(max(lens)-len(x)) for x in perc_2]
    
    finals.append((str('    -'+'-'*(len(perc_list_5)*3)))+"\n")
    tt=''
    for i in range(max(lens)):
        for k in perc_3:
            tt=tt+k[i]+"  "
        finals.append('     '+tt+"\n")
        tt=''
    
    finals[-1]=finals[-1].replace('\n',"")

    return ''.join(finals)