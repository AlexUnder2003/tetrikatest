from collections import Counter


class LetterCountPipeline:
    def __init__(self):
        self.counts = Counter()

    def process_item(self, item, spider):
        name = item.get("name")
        if name:
            letter = name[0].upper()
            self.counts[letter] += 1
        return item

    def close_spider(self, spider):
        # пишем финальный CSV
        with open("beasts.csv", "w", encoding="utf-8") as f:
            for letter, cnt in sorted(self.counts.items()):
                f.write(f"{letter},{cnt}\n")
