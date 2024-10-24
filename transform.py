def transform_data(data):
    cleaned_data = data.dropna()

    cleaned_data["purchased category"] = cleaned_data["purchase amount"].apply(
        lambda x: "High" if x > 100 else "Low"
        )
    
    print("Data transformed successfully.")
    return cleaned_data
