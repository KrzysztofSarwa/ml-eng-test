import json
from typing import List, Tuple
import cv2
import numpy as np
import pandas as pd

def process_walls(image_data):
    """
    This function processes a masked image and detects room regions.

    Args:
        masked_image: A NumPy array representing the masked image.
            Each unique value in the mask represents a different region.

    Returns:
        A dictionary containing the processed results in the specified format.
    """
    # Convert image data to numpy array
    nparr = np.frombuffer(image_data, np.uint8)
    # Decode image
    masked_image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
    
    # Convert to grayscale if necessary
    if masked_image.shape[-1] == 3:  # Check for 3 channels
        masked_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)
        
    # Display the grayscale image (optional)
    #cv2.imshow("Grayscale Image", masked_image)
    #cv2.waitKey(0)  # Wait for key press to close window
    #cv2.destroyAllWindows()    
    #print(np.amax(masked_image))

    # Find contours of unique regions in the mask
    contours, _ = cv2.findContours(masked_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize empty list for room detections
    room_detections = []

    # Loop through each contour (region)
    for idx, contour in enumerate(contours):
        # Convert contour to a list of points
        vertices = contour.reshape(-1, 2).tolist()

        # Calculate convex hull
        hull = cv2.convexHull(np.array(vertices))
        hull_vertices = hull.reshape(-1, 2).tolist()

        confidence = 0.8

        # Create room detection dictionary
        room_detection = {
            "roomId": f"room_{idx+1}",  # Assign unique room ID
            "vertices": hull_vertices,  # Use convex hull vertices
            "confidence": confidence,
        }

        # Append room detection to the list
        room_detections.append(room_detection)

    # Prepare the final response dictionary
    response = {
        "type": "rooms",
        "imageId": "some_image_id", 
        "detectionResults": {"rooms": room_detections},
    }

    return response