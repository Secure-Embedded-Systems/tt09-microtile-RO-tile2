# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Starting test")

    # Set up the clock with a period of 10 us (100 KHz)
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Resetting device")
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    # Test with different `ui_in` values
    for val in [3, 2, 165, 229]:
        dut.ui_in.value = val
        await ClockCycles(dut.clk, 2)
        dut._log.info(f"ui_in: {val}, TDC Output: {dut.uo_out.value}")

    dut._log.info("Test complete")

