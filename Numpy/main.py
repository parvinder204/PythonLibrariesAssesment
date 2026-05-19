from utils import load_image, save_image, show_image
from filters import grayscale, negative, brightness


IMAGE_PATH = "images/sample.png"

def main():
    image = load_image(IMAGE_PATH)
    print("\n=======Numpy Image Filters=======\n")
    print("1. Grayscale")
    print("2. Negative")
    print("3. Brightness")
    print("4. Exit")
    
    choice = input("\nEnter your choice: ")
    if choice == "1":
        result = grayscale(image)
        show_image(result, "Grayscale")
        save_image(result, "output/grayscale.png")
        print("Saved: output/grayscale.png")

    elif choice == "2":
        result = negative(image)
        show_image(result, "Negative")
        save_image(result, "output/negative.png")
        print("Saved: output/negative.png")

    elif choice == "3":
        value = int(input("Brightness value: "))
        result = brightness(image, value)
        show_image(result, "Brightness")
        save_image(result, "output/brightness.png")
        print("Saved: output/brightness.png")

    elif choice == "4":
        print("Goodbye!")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
