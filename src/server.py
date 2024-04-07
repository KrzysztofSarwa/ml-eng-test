from fastapi import FastAPI, File, UploadFile, Query
from image_processing import process_walls
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/run-inference")
async def run_inference(
    type: str = Query(..., description="Type of inference to perform"),
    image: UploadFile = File(...)
):
    # Get image filename
    filename = image.filename

    # Load image data using OpenCV or similar library
    image_data = await image.read()

    # Process image based on specified type
    if type == "room":
        results = process_walls(image_data)
    else:
        return {"error": "Invalid inference type"}
    """elif type == "walls":
        results = process_rooms(image_data)
    elif type == "page_info":
        results = process_page_info(image_data)
    elif type == "tables":
        results = process_tables(image_data)"""

    # Return the processed results
    return JSONResponse(content=results)
