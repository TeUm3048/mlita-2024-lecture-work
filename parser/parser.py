class Parser:
    def __init__(self, input_string):
        self.tokens = list(input_string.replace(" ", ""))
        self.current_token = None
        self.next_token()

    def next_token(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = None

    def parse(self):
        polynom = self.parse_polynom()
        if self.current_token is not None:
            tokens = self.current_token + ''.join(self.tokens)
            raise SyntaxError(f"Unexpected tokens: {tokens}")
        return polynom

    def parse_polynom(self):
        if self.current_token == '0':
            self.next_token()
            return {"type": "Polynom", "zero": True}
        else:
            first_term = self.parse_first_term()
            more_terms = self.parse_more_terms()
            return {
                "type": "Polynom",
                "first_term": first_term,
                "more_terms": more_terms,
            }

    def parse_first_term(self):
        opt_sign = self.parse_opt_sign()
        factor = self.parse_factor()
        return {"type": "FirstTerm", "opt_sign": opt_sign, "factor": factor}

    def parse_more_terms(self):
        if self.current_token in {'+', '-'}:
            operator = self.current_token
            self.next_token()
            factor = self.parse_factor()
            more_terms = self.parse_more_terms()
            return {
                "type": "MoreTerms",
                "operator": operator,
                "factor": factor,
                "more_terms": more_terms,
            }
        else:
            return {"type": "MoreTerms", "epsilon": True}

    def parse_opt_sign(self):
        if self.current_token in {'+', '-'}:
            opt_sign = self.current_token
            self.next_token()
            return opt_sign
        else:
            return None

    def parse_factor(self):
        if self.current_token is None:
            raise SyntaxError("Unexpected end of input in factor")

        if self.current_token.isdigit() and self.current_token != '0':
            proper_integer = self.parse_proper_integer()
            maybe_x_part = self.parse_maybe_x_part()
            return {
                "type": "Factor",
                "proper_integer": proper_integer,
                "maybe_x_part": maybe_x_part,
            }
        elif self.current_token == 'x':
            self.next_token()
            power_part = self.parse_power_part()
            return {"type": "Factor", "x": True, "power_part": power_part}
        else:
            raise SyntaxError(f"Unexpected token in factor: {self.current_token}")

    def parse_maybe_x_part(self):
        if self.current_token == 'x':
            self.next_token()
            power_part = self.parse_power_part()
            return {"type": "MaybeXPart", "x": True, "power_part": power_part}
        else:
            return {"type": "MaybeXPart", "epsilon": True}

    def parse_power_part(self):
        if self.current_token == '^':
            self.next_token()
            proper_integer = self.parse_proper_integer()
            return {"type": "PowerPart", "proper_integer": proper_integer}
        else:
            return {"type": "PowerPart", "epsilon": True}

    def parse_proper_integer(self):
        if self.current_token == '1':
            self.next_token()
            non_empty_digits = self.parse_non_empty_digits()
            return {
                "type": "ProperInteger",
                "starts_with_1": True,
                "digits": non_empty_digits,
            }
        elif self.current_token in '23456789':
            digit2_to_9 = self.current_token
            self.next_token()
            digits = self.parse_digits()
            return {
                "type": "ProperInteger",
                "starts_with_2_to_9": digit2_to_9,
                "digits": digits,
            }
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

    def parse_non_empty_digits(self):
        if self.current_token is None:
            raise SyntaxError(f"Unexpected end of input")
        if self.current_token.isdigit():
            digit = self.current_token
            self.next_token()
            digits = self.parse_digits()
            return [digit] + digits
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token}")

    def parse_digits(self):
        if self.current_token and self.current_token.isdigit():
            digit = self.current_token
            self.next_token()
            digits = self.parse_digits()
            return [digit] + digits
        else:
            return []
