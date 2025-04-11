import questionary


from typing import List


class InputHandler:
    @staticmethod
    def prompt_list(prompt: str,
                   comma_separated: bool = False,
                   default_items: Optional[List[str]] = None) -> List[str]:
        if default_items is None:
            default_items = []

        if comma_separated:
            default_value = ", ".join(default_items)
            answer = questionary.text(
                prompt,
                default=default_value
            ).ask()
            return [item.strip() for item in answer.split(",") if item.strip()]
        else:
            print(prompt)
            items = []
            for i, default_item in enumerate(default_items):
                item = questionary.text(
                    f"[{i+1}]",
                    default=default_item
                ).ask()
                if item:
                    items.append(item)

            while True:
                new_item = questionary.text(
                    f"[{len(items)+1}] (empty to finish)"
                ).ask()
                if not new_item:
                    break
                items.append(new_item)
            return items