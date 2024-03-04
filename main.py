import time
import pyperclip


def format_input(data: str) -> list[str]:
    data = data.replace(",", "\n") # Replace commas with newlines
    return data.splitlines()


def get_unique_instances(data: list[str]) -> list[str]:
    unique_instances = []
    for line in data:
        clean_line = line.lstrip()
        if clean_line in unique_instances:
            continue
        unique_instances.append(clean_line)
    return unique_instances


def create_product(data: list[str]):
    output = []
    unique = get_unique_instances(data)
    unique_clone = unique.copy()

    if len(unique) < 2:
        raise IndexError(unique)
    print(f"Creating product...")

    for _ in unique:
        upper = len(unique_clone) + 1
        i: int = 1
        while i < upper:
            output.append(unique_clone[0:i]) 
            i += 1
        del unique_clone[0]
    return output


def format_output(product: list[list[str]], initial: str = None) -> str:
    output = "" if initial is None else f"{initial}\n"

    product.sort(key=lambda x: len(x))

    for line in product:
        output += f"{', '.join(line)}\n"
    return output.strip()


def get_expected_output_line_count(data):
    length = len(get_unique_instances(data))
    expected_lines = 0
    while length != 0:
        expected_lines += length
        length -= 1
    return expected_lines

def run():
    start = time.time()
    clipboard = pyperclip.paste()
    if clipboard == pyperclip.init_no_clipboard()[0]:
        print("No available clipboard found. Are you sure you copied your data?")
        return
    
    lines = format_input(clipboard)
    print(f"Num lines: {len(lines)}")
    
    try:
        product = create_product(lines)
    except IndexError:
        print("ERROR: Could not create product of input. Does your input have two or more lines?")
        return

    end = time.time()

    print("RESULT: Success! Check your clipboard.")
    print(f"RESULT: Took {round(end-start, 3)}s to complete")
    print(f"RESULT: {len(product)} lines created (expected {get_expected_output_line_count(lines)})")
    pyperclip.copy(format_output(product))


if __name__ == '__main__':
    run()