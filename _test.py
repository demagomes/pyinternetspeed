import csv
import main
import datetime
import os

# Test printheader() output
def test_print_header(capsys):

    # Executes function
    main.printheader()

    # captures the output of the function using capsys from pytest
    captured = capsys.readouterr()
    all_outputs = captured.out.split('\n')

    # test number of rows in the output
    assert len(all_outputs) == 4

    # test each row's content
    assert all_outputs[0] == '\x1b[95mPython Internet Speed Test\x1b[0m'
    assert all_outputs[1] == '\x1b[92mhttps://github.com/demagomes/pyinternetspeed\x1b[0m'
    assert all_outputs[2] == '\x1b[92mPlease press Control+C to end the program\x1b[0m'
    assert all_outputs[3] == ''

# Test cprint function output
def test_cprint(capsys):

    # Executes function
    main.cprint('Unit Test Header','HEADER')

    # captures the output of the function using capsys from pytest
    captured = capsys.readouterr()

     # test output
    assert captured.out== '\x1b[95mUnit Test Header\x1b[0m\n'

# Test getfilename function return
def test_getfilename():
    today = datetime.date.today().strftime("%d-%m-%Y")
    assert main.getfilename() == today + '_internetspeedtestresults.csv'

# Test save saveresultstocsv file contents
def test_saveresultstocsv():
    filename = 'unittest.csv'
    main.saveresultstocsv(filename,'100','10','1')

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        row = next(reader)

        # test for header/fields
        assert reader.fieldnames[0] == 'timestamp'
        assert reader.fieldnames[1] == 'download'
        assert reader.fieldnames[2] == 'upload'
        assert reader.fieldnames[3] == 'ping'
    
        # test the values in the csv
        assert row['download'] == '100'
        assert row['upload'] == '10'
        assert row['ping'] == '1'        
            
        # delete the test csv
        os.remove(filename)