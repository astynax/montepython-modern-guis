import hyperdiv as hd


def main():
    state = hd.state(counter=0)
    hd.h1("Counter")
    with hd.hbox():
        hd.text(state.counter)
        if hd.button("+").clicked:
            state.counter += 1
        elif hd.button("-", disabled=state.counter <= 0).clicked:
            state.counter -= 1


if __name__ == '__main__':
    hd.run(main, index_page=hd.index_page(
        title="Counter",
    ))
