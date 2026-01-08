class MiniPHPInterpreter:
    def __init__(self):
        self.vars = {}
        self.output = []

    def execute(self, code: str) -> str:
        self.vars = {}
        self.output = []

        lines = [
            line.strip()
            for line in code.splitlines()
            if line.strip()
            and not line.strip().startswith("<?")
            and not line.strip().startswith("?>")
        ]

        i = 0
        while i < len(lines):
            line = lines[i]

            # IF condition
            if line.upper().startswith("IF"):
                condition = line[line.find("(")+1 : line.find(")")]
                left, op, right = condition.split()

                left_val = self.vars.get(left, 0)
                right_val = self.vars.get(right, 0)

                condition_result = False
                if op == ">":
                    condition_result = left_val > right_val

                i += 1  # masuk block IF

                if condition_result:
                    while i < len(lines) and lines[i] != "}":
                        self._execute_line(lines[i])
                        i += 1
                    i += 1  # skip }
                    if i < len(lines) and lines[i].upper().startswith("ELSE"):
                        i += 1
                        while i < len(lines) and lines[i] != "}":
                            i += 1
                else:
                    while i < len(lines) and lines[i] != "}":
                        i += 1
                    i += 1
                    if i < len(lines) and lines[i].upper().startswith("ELSE"):
                        i += 1
                        while i < len(lines) and lines[i] != "}":
                            self._execute_line(lines[i])
                            i += 1
                i += 1
                continue

            # normal line
            self._execute_line(line)
            i += 1

        if not self.output:
            return "Program tidak menghasilkan output."

        return "\n".join(self.output)

    def _execute_line(self, line: str):
        line = line.rstrip(";")

        # assignment
        if line.startswith("$") and "=" in line:
            var, value = line.split("=", 1)
            var = var.strip()
            value = value.strip()

            if value.isdigit():
                self.vars[var] = int(value)
            elif value.startswith("$"):
                self.vars[var] = self.vars.get(value, 0)
            else:
                self.vars[var] = value.replace('"', "")

        # PRINT
        elif line.upper().startswith("PRINT"):
            content = line[5:].strip()
            parts = content.split(".")
            result = ""

            for p in parts:
                p = p.strip()
                if p.startswith("$"):
                    result += str(self.vars.get(p, 0))
                else:
                    result += p.replace('"', "")

            self.output.append(result)
