import requests
from bs4 import BeautifulSoup

def get_h3_headings_with_following_p(url):
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()  # Check for any request errors

        soup = BeautifulSoup(response.content, 'html.parser')
        headings_with_paragraphs = []

        h3_headings = soup.find_all('h3')
        for heading in h3_headings:
            # Find the sibling <p> tag immediately following the h3 heading
            next_p = heading.find_next_sibling('p')
            if next_p:
                # Concatenate the h3 heading with the text of the following <p>
                concatenated_text = f"{heading.text.strip()} {next_p.text.strip()}"
                headings_with_paragraphs.append(concatenated_text)

        return headings_with_paragraphs
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

if __name__ == "__main__":
    url = "https://www.fargomoorhead.org/food-drink/article/fargo-moorheads-happy-hour-guide/"
    headings_with_paragraphs = get_h3_headings_with_following_p(url)

    if headings_with_paragraphs:
        print("H3 Headings with following paragraphs:")
        for idx, content in enumerate(headings_with_paragraphs, 1):
            print(f"{idx}. {content}")

        # Write the results to a text file
        output_file = "output.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            for idx, content in enumerate(headings_with_paragraphs, 1):
                file.write(f"{idx}. {content}\n")

        print(f"\nResults have been saved to '{output_file}'.")
    else:
        print("Failed to fetch headings and/or paragraphs.")
