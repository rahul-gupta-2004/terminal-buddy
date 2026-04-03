import sys
import subprocess
import ollama


def get_model_name(model_index):
    try:
        models_info = ollama.list()
        # Updated logic to handle the new Ollama library response structure
        models = [m.model for m in models_info.models]

        if not models:
            print("❌ No local models found in Ollama. Please pull a model first.")
            sys.exit(1)

        try:
            idx = int(model_index) - 1
            if 0 <= idx < len(models):
                selected = models[idx]
            else:
                selected = models[0]
        except (ValueError, IndexError):
            selected = models[0]

        print(f"🤖 Using model: {selected}")
        return selected
    except Exception as e:
        print(f"❌ Error connecting to Ollama: {e}")
        sys.exit(1)


def generate_command(model, prompt):
    system_prompt = (
        "You are a specialized assistant that converts English to Bash commands. "
        "Rules: 1. Output ONLY the command. No explanations. No markdown code blocks. "
        "2. Strictly forbid any commands involving 'sudo'. If asked for sudo, output 'ERROR: Sudo not allowed'. "
        "3. Focus on file operations, searching, and system info."
    )

    response = ollama.generate(model=model, system=system_prompt, prompt=prompt)
    return response["response"].strip()


def main():
    if len(sys.argv) < 2:
        print('Usage: terminal_buddy [model_number] "prompt"')
        return

    # Handle optional model number
    if sys.argv[1].isdigit() and len(sys.argv) > 2:
        model_idx = sys.argv[1]
        user_prompt = " ".join(sys.argv[2:])
    else:
        model_idx = "1"
        user_prompt = " ".join(sys.argv[1:])

    selected_model = get_model_name(model_idx)
    command = generate_command(selected_model, user_prompt)

    if "sudo" in command.lower() or "ERROR" in command:
        print(
            "⚠️ Security Restriction: Sudo commands or administrative privileges are not allowed."
        )
        return

    print(f"AI: {command}")

    confirm = input("Run it? (y/n): ").lower()
    if confirm == "y":
        try:
            # Use shell=True to allow pipes and complex bash syntax
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.stdout:
                print(f">>> {result.stdout.strip()}")
            if result.stderr:
                print(f"Error: {result.stderr.strip()}")
            print("Done ✅")
        except Exception as e:
            print(f"Execution failed: {e}")
    else:
        print("Operation cancelled.")


if __name__ == "__main__":
    main()
