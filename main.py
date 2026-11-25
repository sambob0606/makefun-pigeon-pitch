import os

ENTRY = "Investors, I'm raising seed funding—literally, the park is covered in it—for StatueShield: museums pay us pigeons to aim our poop elsewhere."


def main():
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
