import ollama
import json


class Semantic_Analyzer:
    def __init__(self):
        self.SYSTEM_PROMPT = """
        You are a precision text classification engine. Your sole task is to evaluate user input against exactly seven predefined categories: Technology, Sports, Education, Business, Health, Politics, Entertainment.

        STRICT RULES:
        1. Analyze the semantic content and assign relevance scores to each applicable category.
        2. Return ONLY a valid JSON dictionary matching this exact schema:
        {
            "labels": ["Category1", "Category2", ...],
            "confidence": [integer, integer, ...]
        }
        3. "labels" must contain ONLY terms from the predefined list above.
        4. "confidence" must be an array of integers (0–100) representing relevance strength, matching the order and length of "labels".
        5. PREFER SINGLE-LABEL OUTPUTS. Only return multiple labels if the text clearly and substantially addresses MULTIPLE categories simultaneously. NEVER force additional labels if one category dominates.
        6. NO markdown, NO code fences, NO explanations. Return RAW JSON only.
        7. If the text does not strongly align with any category, assign low confidence (10–25%) to the most plausible one and keep the array minimal. Prioritize accuracy over quantity.
        """

        self.VALID_CATEGORIES = [
            "Technology",
            "Sports",
            "Education",
            "Business",
            "Health",
            "Politics",
            "Entertainment",
        ]

        self.MODEL_NAME = "phi3:3.8b"

    def analyze(self, text: str) -> tuple[list[str], list[int]]:
        # classify the text using llm
        response = ollama.chat(
            model=self.MODEL_NAME,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ],
        ).message.content

        # extracting json from response
        if response.startswith("```json"):
            response = response.replace("```json", "").replace("```", "").strip()

        # converting json response to python dictionary
        response_json = json.loads(response)

        # extracting labels and confidences
        labels = response_json.get("labels", [])
        confidences = response_json.get("confidence", [])

        return (labels, confidences)
