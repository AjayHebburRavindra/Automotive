import cv2
import numpy as np
import json

def load_media(media_path):
    if media_path.endswith(('png', 'jpg', 'jpeg')):
        image = cv2.imread(media_path)
        return image, 'image'
    elif media_path.endswith(('mp4', 'avi', 'mov')):
        video = cv2.VideoCapture(media_path)
        return video, 'video'
    else:
        raise ValueError("Unsupported file format")

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    return edges

output_path = 'output_edges.jpg'


def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)
    polygon = np.array([[
        (0, height),
        (width, height),
        (width, height // 2),
        (0, height // 2),
    ]], np.int32)
    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)
    return cropped_edges

def detect_lines(cropped_edges):
    lines = cv2.HoughLinesP(
        cropped_edges,
        rho=1,
        theta=np.pi / 180,
        threshold=50,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=5
    )
    return lines

def draw_lines(image, lines):
    line_image = np.zeros_like(image)
    lines_list = []
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
                lines_list.append({"x1": x1, "y1": y1, "x2": x2, "y2": y2})
    return line_image, lines_list

def process_frame(frame):
    edges = preprocess_image(frame)
    cropped_edges = region_of_interest(edges)
    lines = detect_lines(cropped_edges)
    line_image, lines_list = draw_lines(frame, lines)
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 0)
    return combo_image, lines_list

def save_to_json(data, json_path):
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)

media_path = r'D:\Masters\FAU-Erlangen\Coding\My_Projects\Lane_detection\test\2.jpg'  # Replace with your file path
json_output_path = r'C:\Users\ajay9\OneDrive\Desktop\test\lane_detection_output.json'  # Replace with your desired JSON output path

media, media_type = load_media(media_path)

output_data = []

if media_type == 'image':
    combo_image, lines_list = process_frame(media)
    output_data.append({"frame": 0, "lines": lines_list})
    cv2.imshow("Lane Detection", combo_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif media_type == 'video':
    frame_number = 0
    while True:
        ret, frame = media.read()
        if not ret:
            break
        frame_with_lanes, lines_list = process_frame(frame)
        output_data.append({"frame": frame_number, "lines": lines_list})
        frame_number += 1
        cv2.imshow("Lane Detection", frame_with_lanes)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    media.release()
    cv2.destroyAllWindows()

# Save the output data to JSON
save_to_json(output_data, json_output_path)
