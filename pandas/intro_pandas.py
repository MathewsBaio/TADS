import pandas as pd

data = ['huguinho', 'zezinho', 'luizinho']

emp_names = pd.Series(data)

email_data = ['huguinho.silva', 'zezinho.pereira', 'luizinho.souza']

emp_emails = pd.Series(email_data)

emp_ids = pd.Series([9001, 9002, 9003], name='ids')

df = pd.concat([emp_ids, emp_names, emp_emails])


df.set_index('ids')