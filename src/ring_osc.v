module ring_osc(
    input wire rst_n,
    input wire clk,
    input wire ro_activate,
    output wire ro_out
);

    reg en;
    (* keep = "true" *) wire q;
    (* keep = "true" *) wire q0;
    (* keep = "true" *) wire q1;
    (* keep = "true" *) wire q2;
    (* keep = "true" *) wire cq2;

    assign ro_out = en ? q : 1'b0;

    always @(posedge clk) begin
        if (ro_activate)
            en <= 1'b1;
        else
            en <= 1'b0;
    end

    assign cq2 = (en & q2);
    (* keep = 1 *) cinv cinv1(.a(cq2), .q(q0));
    (* keep = 1 *) cinv cinv2(.a(q0), .q(q1));
    (* keep = 1 *) cinv cinv3(.a(q1), .q(q2));
    assign q = q2;
endmodule

