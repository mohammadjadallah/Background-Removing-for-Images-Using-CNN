# Importing Required Modules
from rembg import remove
from PIL import Image

# Store path of the image in the variable input_path
input_path = 'kid.jpg'

# Store path of the output image in the variable output_path
output_path = 'output.png'

# Processing the image
input = Image.open(input_path)

# Removing the background from the given Image
output = remove(input)

#Saving the image in the given path
output.save(output_path)
print("image saved...")

# import cv2
# import mediapipe as mp

# # Initialize MediaPipe Hands model
# mp_hands = mp.solutions.hands

# # Initialize video capture
# cap = cv2.VideoCapture(0)

# # Initialize the drawing utilities
# mp_drawing = mp.solutions.drawing_utils

# # Start capturing and processing frames
# with mp_hands.Hands(
#     static_image_mode=False,
#     max_num_hands=2,
#     min_detection_confidence=0.5) as hands:
#     while cap.isOpened():
#         # Read frame from camera
#         success, image = cap.read()
#         if not success:
#             break

#         # Convert the image to RGB and process it with MediaPipe Hands
#         image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
#         results = hands.process(image)
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#         # Draw hand landmarks on the image
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(
#                     image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#         # Display the resulting image
#         cv2.imshow('MediaPipe Hands', image)
#         if cv2.waitKey(5) & 0xFF == 27:
#             break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()
