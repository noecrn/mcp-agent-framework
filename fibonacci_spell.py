#!/usr/bin/env python3
"""
🔮 The Fibonacci Enchantment 🔮
A magical scroll by Kiro the Grey Hat

This ancient spell reveals the sacred sequence where each number
is born from the union of its two predecessors, following the
eternal pattern discovered by the mathematician-wizard Leonardo Fibonacci.
"""

def fibonacci_spell(n=10):
    """
    Cast the Fibonacci incantation to generate the first n numbers
    of the mystical sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
    
    Args:
        n (int): Number of Fibonacci numbers to conjure (default: 10)
    
    Returns:
        list: The first n numbers of the Fibonacci sequence
    """
    print("✨ Casting the Fibonacci Spell... ✨")
    print("🌟 Summoning the ancient sequence... 🌟")
    print()
    
    # Initialize the magical sequence
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    # Begin the incantation
    fibonacci_numbers = [0, 1]
    
    # Weave the spell for remaining numbers
    for i in range(2, n):
        next_number = fibonacci_numbers[i-1] + fibonacci_numbers[i-2]
        fibonacci_numbers.append(next_number)
        print(f"🔥 Conjuring number {i+1}: {next_number}")
    
    return fibonacci_numbers

def display_magical_sequence(sequence):
    """Display the conjured sequence in a mystical format"""
    print("\n" + "="*50)
    print("🌙 THE FIBONACCI PROPHECY HAS BEEN REVEALED! 🌙")
    print("="*50)
    print(f"📜 The Sacred Sequence: {sequence}")
    print()
    
    # Show the magical pattern
    print("🔮 Behold the Pattern of Creation:")
    for i, num in enumerate(sequence):
        stars = "⭐" * min(num, 10)  # Visual representation (capped for readability)
        print(f"   Position {i}: {num} {stars}")
    
    print("\n💫 The spell is complete! The universe's mathematical")
    print("   harmony has been unveiled through ancient wizardry! 💫")

if __name__ == "__main__":
    # Cast the spell to reveal the first 10 Fibonacci numbers
    mystical_sequence = fibonacci_spell(10)
    display_magical_sequence(mystical_sequence)
    
    print("\n🧙‍♂️ Kiro the Grey Hat's signature magic ✨")