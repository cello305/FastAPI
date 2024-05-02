from fastapi import FastAPI
from app.db.supabase import create_supabase_client

app = FastAPI()

# Initialize Supabase client
supabase = create_supabase_client()

@app.get("/{id}")
async def getBody(id: int):
    try:
        # Fetch user data with ID 1 from the "sourceData" table
        response = supabase.table("sourceData").select("body").eq("id", id).execute()
        
        # Log the complete response from Supabase
        body_content = response.data[0].get('body', None)
        if body_content:
            return body_content
        else:
            return {"message": "User not found"}
    except Exception as e:
        return {"message": f"User retrieval failed: {str(e)}"}

@app.post('/add')
async def addBody(body: str):
    try:
        # Insert the body content into the "sourceData" table
        response = supabase.table("sourceData").insert([{"body": body}]).execute()
    except Exception as e:
        return {"message": f"User insertion failed: {str(e)}"}