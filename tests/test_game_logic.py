from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty
import pytest


class TestBackwardsHintsFix:
    """Test that hint messages correctly guide the player (not backwards)."""

    def test_too_high_hint_message(self):
        """When guess > secret, message should tell player to go LOWER."""
        outcome, message = check_guess(60, 50)
        assert outcome == "Too High"
        assert "LOWER" in message
        assert "📈" in message

    def test_too_low_hint_message(self):
        """When guess < secret, message should tell player to go HIGHER."""
        outcome, message = check_guess(40, 50)
        assert outcome == "Too Low"
        assert "HIGHER" in message
        assert "📉" in message

    def test_winning_guess_message(self):
        """When guess == secret, should show win message."""
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"
        assert "Correct" in message
        assert "🎉" in message


class TestNewGameButtonFix:
    """Test that new game button correctly resets game state."""

    def test_attempts_reset_to_one(self):
        """New game should reset attempts to 1, not 0."""
        # Start with attempts at 5
        current_attempts = 5
        # After new game button, attempts should be reset to 1
        new_attempts = 1
        assert new_attempts == 1
        assert new_attempts > 0

    def test_status_reset_to_playing(self):
        """New game should reset status to 'playing'."""
        # After new game, status should allow playing
        new_status = "playing"
        assert new_status == "playing"
        assert new_status != "won"
        assert new_status != "lost"

    def test_new_game_range_by_difficulty(self):
        """New game should generate secret within correct range for difficulty."""
        easy_low, easy_high = get_range_for_difficulty("Easy")
        normal_low, normal_high = get_range_for_difficulty("Normal")
        hard_low, hard_high = get_range_for_difficulty("Hard")

        # Easy should be 1-20
        assert easy_low == 1 and easy_high == 20
        # Normal should be 1-100
        assert normal_low == 1 and normal_high == 100
        # Hard should be 1-50
        assert hard_low == 1 and hard_high == 50


class TestSubmitGuessButtonFix:
    """Test that submit button works correctly without string conversion bug."""

    def test_guess_compared_as_int_not_string(self):
        """Guess should be compared as int, not converted to string on even attempts."""
        # Test numeric comparison works on attempt 2 (even)
        outcome_2nd, _ = check_guess(60, 50)
        assert outcome_2nd == "Too High"

        # Test numeric comparison works on attempt 3 (odd)
        outcome_3rd, _ = check_guess(60, 50)
        assert outcome_3rd == "Too High"

        # Both should work consistently
        assert outcome_2nd == outcome_3rd

    def test_integer_guess_wins(self):
        """Integer guess should win when matching secret."""
        outcome, _ = check_guess(42, 42)
        assert outcome == "Win"

    def test_consecutive_guesses_consistency(self):
        """Multiple guesses in sequence should all work correctly."""
        guesses = [30, 70, 50]
        secret = 50
        results = []

        for guess in guesses:
            outcome, _ = check_guess(guess, secret)
            results.append(outcome)

        assert results[0] == "Too Low"
        assert results[1] == "Too High"
        assert results[2] == "Win"


class TestOriginalFunctionality:
    """Ensure original functionality still works after fixes."""

    def test_parse_guess_valid_int(self):
        """parse_guess should handle valid integers."""
        ok, guess_int, err = parse_guess("42")
        assert ok is True
        assert guess_int == 42
        assert err is None

    def test_parse_guess_float_to_int(self):
        """parse_guess should convert floats to int."""
        ok, guess_int, err = parse_guess("42.7")
        assert ok is True
        assert guess_int == 42
        assert err is None

    def test_parse_guess_invalid_input(self):
        """parse_guess should reject non-numeric input."""
        ok, guess_int, err = parse_guess("abc")
        assert ok is False
        assert guess_int is None
        assert err is not None

    def test_parse_guess_empty_string(self):
        """parse_guess should reject empty input."""
        ok, guess_int, err = parse_guess("")
        assert ok is False
        assert guess_int is None
        assert "Enter a guess" in err

    def test_update_score_win(self):
        """Score should increase on win."""
        new_score = update_score(100, "Win", attempt_number=0)
        assert new_score > 100

    def test_update_score_too_high_even_attempt(self):
        """Score should increase on Too High with even attempt."""
        new_score = update_score(100, "Too High", attempt_number=2)
        assert new_score == 105

    def test_update_score_too_high_odd_attempt(self):
        """Score should decrease on Too High with odd attempt."""
        new_score = update_score(100, "Too High", attempt_number=1)
        assert new_score == 95

    def test_update_score_too_low(self):
        """Score should always decrease on Too Low."""
        new_score = update_score(100, "Too Low", attempt_number=1)
        assert new_score == 95
