PYTHON ?= python3

.PHONY: run run-ai serve test

run:
	$(PYTHON) -m ckb_talk_radar --hours 24 --skip-ai

run-ai:
	$(PYTHON) -m ckb_talk_radar --hours 24

serve:
	$(PYTHON) -m ckb_talk_radar --serve-only --output-dir outputs --port 8000

test:
	$(PYTHON) -m unittest discover -s tests -v
