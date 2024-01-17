import pandas as pd

df = pd.read_csv('cafeLeads - leads.csv')
print(df)

def addData(userName, userNumber, userEmail):
    name = userName
    number = userNumber
    email = userEmail

    user_data = {
        'name': [name],
        'number': [number],
        'email': [email]
    }

    sub_df = pd.DataFrame(user_data, index=[0])

    existing_data = pd.read_csv('cafeLeads - leads.csv')

    updated_data = pd.concat([existing_data, sub_df], ignore_index=True)

    updated_data.to_csv('cafeLeads - leads.csv', index=False)
