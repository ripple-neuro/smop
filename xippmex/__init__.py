import smop.core
import xipppy
import atexit

# Putting open here is probably not the right approach but may be needed
# for compatibility with MATLAB scripts.
xipppy.open()

atexit.register(xipppy.close)

def xippmex(*args):
    """
    basic entry point for xippmex function.  This will be mapped to other worker
    functions below.
    """
    assert(len(args) >= 1)
    if args[0] == 'time':
        return xipppy.time()
    elif args[0] == 'cont':
        return cont(*args[1:])
    elif args[0] == 'stimseq':
        stimseq(*args[1:])
    # elif args[0] == 'stim':
    # stim(

def cont(*args):
    elecs = args[0]
    # duration specified in ms.
    dur = float(args[1])
    stream = args[2]
    # requesting start time is an optional parameter.  If
    # not specified we but in zero.
    if (len(args) == 4):
        tstart = args[3]
    else:
        tstart = 0

    if stream == 'lfp':
        npoints = int(dur)
        func = xipppy.cont_lfp
    elif stream == 'raw':
        npoints = int(dur * 30)
        func = xipppy.cont_raw
    elif stream == 'hires':
        npoints = int(dur * 2)
        func = xipppy.cont_hires
    elif stream == 'hifreq':
        npoints = int(dur * 7.5)
        func = xipppy.cont_hifreq

    r = func(npoints, elecs, tstart)
    return len(r[0]), r[0], 0

def convert_struct_bits(s):
    return 0

def stimseq(*args):
   
    if type(args[0]) == smop.core.struct:
        # Handle the case where a single struct is MATLAB is passed.  The send
        # function will always treat these as an array, so we pack this in an 
        # extra layer for now.
        _seq_list = [args[0]]
    else:
        _seq_list = args[0]
    seq = []
    for i, s in enumerate(_seq_list):
        seq.append(xipppy.StimSeq(s.elec, s.period, s.repeats, 0))
        # assert(len(s.seq) >= 1)
        for w in s.seq:
            seq[i].add_control_word(w.length, w.ampl, w.pol, w.enable,
                                    w.ampSelect, w.delay, w.fs)
    xipppy.StimSeq.send_stim_seq(seq)
