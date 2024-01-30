import main

# First test (WIP)
def test_print_header(capsys):
    main.printheader()
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')

    # test number of rows in the output
    assert len(all_outputs) == 4

    # test each row's content
    assert all_outputs[0] == "\x1b[95mPython Internet Speed Test\x1b[0m"
    assert all_outputs[1] == "\x1b[92mhttps://github.com/demagomes/pyinternetspeed\x1b[0m"
    assert all_outputs[2] == "\x1b[92mPlease press Control+C to end the program\x1b[0m"
    assert all_outputs[3] == ""
