from semantic_analyzer import Semantic_Analyzer

if __name__ == "__main__":
    analyzer = Semantic_Analyzer()

    print("Semantic Analyzer Started\n")

    while True:
        prompt = input("enter text: ")

        if prompt.lower() == "exit":
            print("\nBot: Bye!")
            break

        labels, confidences = analyzer.analyze(prompt)

        for label, confidence in zip(labels, confidences):
            print(f"\nBot: label: {label}, confidence: {confidence}")
        print()
