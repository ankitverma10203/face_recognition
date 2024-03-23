import os
import face_recognition as fr


def save_image(picture, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)

    if picture:
        with open(directory + filename + ".jpg", "wb") as f:
            f.write(picture.getvalue())


def delete_image(image_path):
    if os.path.exists(image_path):
        os.remove(image_path)


def get_all_images(directory):
    return [file for file in os.listdir(directory) if file.endswith('.jpg') or file.endswith('.png')]


def compare_faces_in_directory(known_image_dir, unknown_image_dir):
    # Get list of image files in the directory
    known_image_files = get_all_images(known_image_dir)
    unknown_image_files = get_all_images(unknown_image_dir)

    if not unknown_image_files:
        return False, -1

    # Iterate over image files
    for j, known_image_file in enumerate(known_image_files):
        # Load images
        unknown_img_path = os.path.join(unknown_image_dir, unknown_image_files[0])
        known_img_path = os.path.join(known_image_dir, known_image_file)
        image1 = fr.load_image_file(unknown_img_path)
        image2 = fr.load_image_file(known_img_path)

        # Find face encodings
        face_encodings1 = fr.face_encodings(image1)
        face_encodings2 = fr.face_encodings(image2)

        if len(face_encodings1) > 0 and len(face_encodings2) > 0:
            # Compare the first face encoding from each image
            face_encoding1 = face_encodings1[0]
            face_encoding2 = face_encodings2[0]

            # Calculate similarity
            similarity = fr.face_distance([face_encoding1], face_encoding2)

            # Set a threshold for similarity
            threshold = 0.4

            # Output comparison result
            user_id = os.path.splitext(known_image_file)[0]
            if similarity[0] < threshold:
                print(f"Images {unknown_image_files[0]} and {known_image_file} have similar faces.")
                return True, user_id
            else:
                print(f"Images {unknown_image_files[0]} and {known_image_file} do not have similar faces.")
        else:
            print(f"No faces found in one or both images.")

    return False, -1
